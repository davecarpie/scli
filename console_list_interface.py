import curses
import sys

class ConsoleListInterface(object):

    def __init__(self, data):
        self.data = data

        self.current_selection_index = 0
        self.highlighted_index = 0
        self.shift = 0

        self.init_keyhandlers()

        self.screen = curses.initscr()
        curses.noecho()
        curses.curs_set(0)
        self.screen.keypad(1)

        self.height, self.width = self.screen.getmaxyx()
        self.draw()


    def draw(self):
        self.screen.clear()

        draw_y_index = 0
        lines = self.current_lines()
        for line in lines:
            self.screen.addstr(draw_y_index, 0, str(line))
            draw_y_index += 1

        self.screen.chgat(self.highlighted_index, 0, self.width, curses.A_REVERSE)


    def current_lines(self):
        if len(self.data) <= self.height:
            return [str(item) for item in self.data]


        if self.shift == 0:
            lines = [str(item) for item in self.data[:self.height-1]] + \
                ["\t\t{} more lines below...".format(len(self.data)-(self.height-1))]
        elif self.shift == len(self.data) - self.height + 1:
            lines = ["\t\t{} more lines above...".format(self.shift)] + \
                [str(item) for item in self.data[self.shift:]]
        else:
            lines = ["\t\t{} more lines above...".format(self.shift)] + \
                [str(item) for item in self.data[self.shift:self.shift+self.height-2]] + \
                ["\t\t{} more lines below...".format(len(self.data)-self.shift - (self.height-2))]

        return lines

    def init_keyhandlers(self):
        self.keyhandlers = {
            ord("q") : self.quit,
            curses.KEY_DOWN : self.move_down,
            curses.KEY_UP : self.move_up
        }

    def move_up(self):
        if self.current_selection_index == 0:
            return

        if self.highlighted_index == 1 and self.current_selection_index != 1:
            if self.shift == 2:
                self.shift = 0
            else:
                self.shift -= 1

            self.current_selection_index -= 1    
        else:
            self.current_selection_index -= 1
            self.highlighted_index -= 1
        
        self.draw()


    def move_down(self):
        if self.current_selection_index == len(self.data) - 1:
            return

        if self.highlighted_index == self.height - 2 and self.current_selection_index != len(self.data) - 2:
            if self.shift == 0:
                self.shift = 2
            else:
                self.shift += 1

            self.current_selection_index += 1
        else:
            self.current_selection_index += 1
            self.highlighted_index += 1

        self.draw()


    def quit(self):
        sys.exit()


    def mainloop(self):
        while True:
            event = self.screen.getch()
            if event in self.keyhandlers:
                self.keyhandlers[event]()

