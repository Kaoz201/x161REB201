import pysvg.structure
import pysvg.builders
import pysvg.text

svg_document = pysvg.structure.svg()

shape_builder = pysvg.builders.ShapeBuilder()

svg_document.addElement(shape_builder.createRect(0, 0,
                                                 "200px", "100px",
                                                 strokewidth = 1,
                                                 stroke = "black",
                                                 fill = "rgb(255, 255, 0)"))

svg_document.addElement(pysvg.text.text("Hello World",
                                        x = 210, y = 110))

print(svg_document.getXML())

svg_document.save("228.svg")
