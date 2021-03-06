# -*- coding: utf-8 -*-
import win32serviceutil
import win32service
import win32event
import server
import os
import sys
import options
class NVDARemoteService(win32serviceutil.ServiceFramework):
	_svc_name_ = "NVDARemoteService"
	_svc_display_name_ = "NVDARemote relay server"
	_svc_deps_ = []
	def __init__(self, args):
		options.setup()
		server.logfile=options.logfile
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
		self.srv=server.Server()

	def SvcStop(self):
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
		self.srv.running=False
		win32event.SetEvent(self.hWaitStop)

	def SvcDoRun(self):
		self.srv.run()
