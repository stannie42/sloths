# -*- coding: utf-8 -*-
""" Sloths: REST API for NoSQL DocumentStore auto-managed.
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import signal

class Sloths(object):
    def __init__(self, stdin_path, stdout_path, stderr_path, pidfile_path, pidfile_timeout):
        self.stdin_path = stdin_path
        self.stdout_path = stdout_path
        self.stderr_path = stderr_path
        self.pidfile_path = pidfile_path
        self.pidfile_timeout = pidfile_timeout

    def run(self):
        while True:
            signal.pause()
