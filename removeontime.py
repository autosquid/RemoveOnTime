# -*- coding: UTF-8 -*-
import time
import win32serviceutil
import win32service
import win32event
import win32evtlogutil
import os.path
import shutil


class RemoveOnTimeService(win32serviceutil.ServiceFramework):
    _svc_name_ = "RemoveOnTime"
    _svc_display_name_ = "RemoveOnTime"
    _svc_description_ = "remove junkdrawer fold every day"
    _svc_deps_ = ["EventLog"]

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.timeout = 1000 * 60 * 60 * 24
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        import servicemanager

        # syncLocalTime()

        while 1:
        # Write a 'started' event to the event log...
            win32evtlogutil.ReportEvent(
                self._svc_name_,
                servicemanager.PYS_SERVICE_STARTED,
                0,  # category
                servicemanager.EVENTLOG_INFORMATION_TYPE,
                                       (self._svc_name_, '')
            )

        # wait for beeing stopped...
            rc = win32event.WaitForSingleObject(self.hWaitStop, self.timeout)

            if rc == win32event.WAIT_OBJECT_0:
            # stop
        # and write a 'stopped' event to the event log.
                win32evtlogutil.ReportEvent(
                    self._svc_name_,
                    servicemanager.PYS_SERVICE_STOPPED,
                    0,  # category
                    servicemanager.EVENTLOG_INFORMATION_TYPE,
                                           (self._svc_name_, '')
                )
                break
            else:
                removefolder()


def removefolder():
    for dirpath, dirname, filenames in os.walk(r'E:\MyDocument\junkdrawer'):
        for p in dirname + filenames:
            f = dirpath + os.sep + p
            mtime = os.path.getmtime(f)
            ttime = time.time()
            if ttime - mtime < 60 * 60 * 24 * 7:
                continue
            try:
                os.remove(f)
            except:
                pass

            try:
                shutil.rmtree(f, ignore_errors=True)
            except:
                pass

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(RemoveOnTimeService)
    # removefolder()
