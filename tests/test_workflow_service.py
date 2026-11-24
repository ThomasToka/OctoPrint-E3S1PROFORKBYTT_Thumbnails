import importlib.util
import os
import re
import unittest
from unittest.mock import Mock


MODULE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "octoprint_e3s1proforkbyttthumbnails",
    "services",
    "workflow_service.py",
)
SPEC = importlib.util.spec_from_file_location("workflow_service", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)
WorkflowService = MODULE.WorkflowService


class WorkflowServiceTests(unittest.TestCase):
    def _service(self, file_manager, printer):
        printer_sync_service = Mock()
        return WorkflowService(
            logger=Mock(),
            settings_plugin=Mock(),
            file_manager=file_manager,
            printer=printer,
            plugin_data_folder_getter=Mock(),
            plugin_identifier="e3s1proforkbyttthumbnails",
            helper_basename="OCTODGUS.GCO",
            regex_extension=re.compile(r"\.gcode$"),
            thumbnail_service=Mock(),
            helper_file_service=Mock(),
            printer_sync_service_getter=Mock(return_value=printer_sync_service),
        )

    def test_transfer_done_reselects_with_job_api(self):
        file_manager = Mock()
        job = object()
        file_manager.create_job.return_value = job
        printer = Mock()
        service = self._service(file_manager, printer)
        service.active_transfer_job_path = "prints/example.gcode"
        service.active_helper_inflight = True

        service.handle_helper_transfer_done({"local": "octodgus.gco"})

        file_manager.create_job.assert_called_once_with(
            "local", "prints/example.gcode"
        )
        printer.set_job.assert_called_once_with(job, print_after_select=False)
        printer.select_file.assert_not_called()

    def test_transfer_done_reselects_absolute_path_without_job_api(self):
        file_manager = Mock(spec=["path_on_disk"])
        file_manager.path_on_disk.return_value = "/uploads/prints/example.gcode"
        printer = Mock(spec=["select_file", "commands"])
        service = self._service(file_manager, printer)
        service.active_transfer_job_path = "prints/example.gcode"
        service.active_helper_inflight = True

        service.handle_helper_transfer_done({"local": "octodgus.gco"})

        file_manager.path_on_disk.assert_called_once_with(
            "local", "prints/example.gcode"
        )
        printer.select_file.assert_called_once_with(
            "/uploads/prints/example.gcode", False, False
        )


if __name__ == "__main__":
    unittest.main()
