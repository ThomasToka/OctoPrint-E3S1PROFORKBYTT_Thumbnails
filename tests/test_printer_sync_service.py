import importlib.util
import os
import tempfile
import unittest
from unittest.mock import Mock


MODULE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "octoprint_e3s1proforkbyttthumbnails",
    "services",
    "printer_sync_service.py",
)
SPEC = importlib.util.spec_from_file_location("printer_sync_service", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
PrinterSyncService = MODULE.PrinterSyncService


class PrinterSyncServiceTests(unittest.TestCase):
    def test_readiness_prefers_current_storage_api(self):
        printer = Mock()
        printer.is_operational.return_value = True
        printer.is_printing.return_value = False
        printer.is_paused.return_value = False
        printer.is_storage_mounted.return_value = True
        service = PrinterSyncService(Mock(), printer, Mock())

        self.assertTrue(service.is_ready_for_helper_upload())
        printer.is_storage_mounted.assert_called_once_with()
        printer.is_sd_ready.assert_not_called()

    def test_readiness_falls_back_to_legacy_sd_api(self):
        printer = Mock(
            spec=[
                "is_operational",
                "is_printing",
                "is_paused",
                "is_sd_ready",
            ]
        )
        printer.is_operational.return_value = True
        printer.is_printing.return_value = False
        printer.is_paused.return_value = False
        printer.is_sd_ready.return_value = True
        service = PrinterSyncService(Mock(), printer, Mock())

        self.assertTrue(service.is_ready_for_helper_upload())
        printer.is_sd_ready.assert_called_once_with()

    def test_send_helper_uses_local_storage_path_and_remote_helper_name(self):
        logger = Mock()
        printer = Mock()
        printer.is_operational.return_value = True
        printer.is_printing.return_value = False
        printer.is_paused.return_value = False
        printer.is_storage_mounted.return_value = True
        printer.is_sd_ready.return_value = True
        printer.get_sd_files.return_value = []
        printer.add_sd_file.return_value = "OCTODGUS.GCO"

        file_manager = Mock()
        file_manager.path_in_storage.return_value = "example.gcode.thumb"
        service = PrinterSyncService(logger, printer, file_manager)

        with tempfile.NamedTemporaryFile() as helper:
            result = service.send_helper_to_sd(helper.name, "OCTODGUS.GCO")

        self.assertTrue(result)
        file_manager.path_in_storage.assert_called_once_with("local", helper.name)
        printer.add_sd_file.assert_called_once_with(
            "example.gcode.thumb",
            "OCTODGUS.GCO",
            tags={
                "source:plugin",
                "plugin:e3s1proforkbyttthumbnails",
                "trigger:thumbnail_helper_sync",
            },
        )

    def test_send_helper_uses_legacy_sd_upload_argument_order(self):
        logger = Mock()
        printer = Mock(
            spec=[
                "is_operational",
                "is_printing",
                "is_paused",
                "is_sd_ready",
                "get_sd_files",
                "add_sd_file",
            ]
        )
        printer.is_operational.return_value = True
        printer.is_printing.return_value = False
        printer.is_paused.return_value = False
        printer.is_sd_ready.return_value = True
        printer.get_sd_files.return_value = []
        printer.add_sd_file.return_value = "OCTODGUS.GCO"

        file_manager = Mock()
        service = PrinterSyncService(logger, printer, file_manager)

        with tempfile.NamedTemporaryFile() as helper:
            result = service.send_helper_to_sd(helper.name, "OCTODGUS.GCO")

        self.assertTrue(result)
        file_manager.path_in_storage.assert_not_called()
        printer.add_sd_file.assert_called_once_with(
            "OCTODGUS.GCO",
            helper.name,
            tags={
                "source:plugin",
                "plugin:e3s1proforkbyttthumbnails",
                "trigger:thumbnail_helper_sync",
            },
        )


if __name__ == "__main__":
    unittest.main()
