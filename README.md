# scli
A selectable, scrollable list interface for terminal applications built using curses.
I extracted this from another project of mine so I could reuse it easier for more projects.

![screenshot](http://i.imgur.com/PEi3Q98.png)

## How to use scli
Copy the source file into your project however you want. I couldn't be bothered coming up with a better way so this will have to do sorry.

If you want to use the selectable version of the list interface then your data objects will need to have a boolean field named `selected` and should implement the `__repr__` method which returns a string that shows the selected status of the object.

### Example usage
Assuming you have a class like the `SelectableInt` class below:
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

Then the interface can be created using
```
nums = [SelectableInt(x) for x in range(1,31)]
interface = SelectableConsoleListInterface(nums).mainloop()
```

When the interface is running, pressing `q` will quit, the up and down arrows will move the selection and pressing `x` will selected the highlighted row.

## Contributing and License
Not really to sure what either of these things are but everyone seems to have them in their repositories. Use this how ever you want. If you wanna add something submit a pull request and I'll merge it in :)
