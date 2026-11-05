import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        if sides < 3: 
            raise ValueError("less than 3 sides")
        if side_length <= 0: 
            raise ValueError("less than 0 length")
        if pen_size <= 0: 
            raise ValueError("less than 0 pen size")
            
        self.x = x
        self.y = y
        self.sides = sides
        self.side_length = side_length
        self.color = color
        self.pen_size = pen_size
        self.angle = angle
        
        self.pen = turtle.Turtle()
        self.pen.hideturtle()  # Optional: hides the turtle cursor for cleaner drawing

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.setheading(self.angle)
        self.pen.pencolor(self.color)
        self.pen.pensize(self.pen_size)
        self.pen.pendown()
        
        for _ in range(self.sides):
            self.pen.forward(self.side_length)
            self.pen.left(360 / self.sides)
            
        self.pen.penup()

    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        self.x = x
        self.y = y
        self.pen.clear()
        self.draw()