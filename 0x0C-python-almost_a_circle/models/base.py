#!/usr/bin/python3
"""base
Defining the base model class
"""
import json
import csv
import turtle


class Base:
    """
    class to manage all other classes in project
    and to avoid duplicating code
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instatiation.
        Initialises a new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the json string of the list_disctonaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the json string of the list_objs to a file.
        """
        t = []
        if list_objs is not None:
            for i in list_objs:
                t.append(i.to_dictionary())
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string(t))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of JSON string of json_string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        return an instance with all the attributes set
        """
        if cls.__name__ == "Square":
            m = cls(5)
        elif cls.__name__ == "Rectangle":
            m = cls(5, 5)
        m.update(**dictionary)
        return m

    @classmethod
    def load_from_file(cls):
        """
        Reads file and returnslist of instances that
        exist in file
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                ls = cls.from_json_string(f.read())
                t = []
                for i in ls:
                    t.append(cls.create(**i))
                return t
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes attributes of list_objs to a csv file
        """
        with open(cls.__name__ + ".csv", "w") as f:
            cwriter = csv.writer(f, delimiter=',')
            for obj in list_objs:
                my_l = []
                if cls.__name__ == "Rectangle":
                    my_l.append(obj.id)
                    my_l.append(obj.width)
                    my_l.append(obj.height)
                    my_l.append(obj.x)
                    my_l.append(obj.y)
                elif cls.__name__ == "Square":
                    my_l.append(obj.id)
                    my_l.append(obj.size)
                    my_l.append(obj.x)
                    my_l.append(obj.y)
                cwriter.writerow(my_l)

    @classmethod
    def load_from_file_csv(cls):
        """
        Reads a cvs file and returns the list of instances
        that exist int eh file
        """
        try:
            with open(cls.__name__ + ".cvs", "r") as f:
                rs = cvs.reader(f, delimiter)
                t = []
                if cls.__name__ == "Rectangle":
                    for i in rs:
                        r = cls(
                                int(i[1]),
                                int(i[2]),
                                int(i[3]),
                                int(i[4]),
                                int(i[0])
                                )
                        t.append(r)
                    return t
                elif cls.__name__ == "Square":
                    for i in rs:
                        r = cls(
                                int(i[1]),
                                int(i[2]),
                                int(i[3]),
                                int(i[0])
                                )
                        t.append(r)
                        return t
        except Exception:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw Rectangles and Squares using the turtle module.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
                turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
