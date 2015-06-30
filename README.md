# scli
A selectable, scrollable list interface for terminal applications built using curses.
I extracted this from another project of mine so I could reuse it easier for more projects.

![screenshot](http://i.imgur.com/PEi3Q98.png)

As you likely have other things that you want to display in the screen the list doesn't normally occupy the whole terminal. The list user interface is created by passing a window to the constructor which we suggest creating using `curses.newwin()`

## How to use scli
Copy the source file into your project however you want. I couldn't be bothered coming up with a better way so this will have to do sorry.

If you want to use the selectable version of the list interface then your data objects will need to have a boolean field named `selected` and should implement the `__repr__` method which returns a string that shows the selected status of the object.

### Example usage
Assuming you have a class like the `SelectableInt` class below...
``` python
class SelectableInt():
	def __init__(self, num):
		self.num = num
		self.selected = False
	def __repr__(self):
		if self.selected:
			return "[x] {}".format(self.num)
		else:
			return "[ ] {}".format(self.num)
```
and you already have a curses window created then, figure out which screen space you want the list to occupy. In the example below we leave room for a header at the top of the window of height `HEADER_HEIGHT`

```python
begin_y = HEADER_HEIGHT; begin_x = 0;
l_height, l_width = screen.getmaxyx()
l_height = l_height - HEADER_HEIGHT

win = curses.newwin(l_height, l_width, begin_y, begin_x)
data = [SelectableInt(x) for x in range(1,21)]
self.list_ui = SelectableConsoleListInterface(win, data)
```

When the interface is running, pressing `q` will quit, the up and down arrows will move the selection and pressing `x` will selected the highlighted row.

## Contributing and License
Not really to sure what either of these things are but everyone seems to have them in their repositories. Use this how ever you want. If you wanna add something submit a pull request and I'll merge it in :)
