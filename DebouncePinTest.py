#By Erick Chicatto
#This is for learning purposes
#3 Jan 2025 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import pyb

def wait_pin_change(pin):
    #Wait for pin to change the value
    #Need to be stable for a continuos 20 ms
    cur_val = pin.value()
    active = 0
    while active < 20:
        if pin.value() != cur_val:
            active += 1
        else:
            active = 0
        pyb.delay(1)


pin_x1 = pyb.Pin('X1', pyb.Pin.IN, pyb.Pin.PULL_DOWN)

while True:
    wait_pin_change(pin_x1)
    pyb.LED(4).toggle()
    



    