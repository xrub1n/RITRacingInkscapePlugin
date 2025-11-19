import inkex


class SetBoxPrototype1Extension(inkex.Effect):
    def add_arguments(self, pars):
        """Add extension parameters."""  
        pars.add_argument("--text_content", type=str, default="Sample Text", help="Text to display")

        pars.add_argument("--box_color", type=str, dest="box_color", default="1", help="Bar for options")
        pars.add_argument("--border_color", type=str, dest="border_color", default="4", help="Bar for options")

        pars.add_argument("--green_color", type=inkex.Color, default=inkex.Color("#b6d6a8"), help="Color green")  #setting each color up as a variable so it can be passed into other functions
        pars.add_argument("--blue_color", type=inkex.Color, default=inkex.Color("#69a4d9"), help="Color blue")
        pars.add_argument("--pink_color", type=inkex.Color, default=inkex.Color("#b665a8"), help="Color pink")
        pars.add_argument("--white_color", type=inkex.Color, default=inkex.Color("#FFFFFF"), help="Color white")
        pars.add_argument("--black_color", type=inkex.Color, default=inkex.Color("#000000"), help="Color black")

        pars.add_argument("--box_width", type=int, default=60, help="Box width")
        pars.add_argument("--box_height", type=int, default=20, help="Box height")
        pars.add_argument("--text_size", type=int, default=7.5, help="Font size")

    def effect(self):
        """Main effect method called when extension is executed."""
        # Get parameters
        text_content = self.options.text_content

        box_color = self.options.box_color   
        border_color = self.options.border_color

        green_color = self.options.green_color
        blue_color = self.options.blue_color
        pink_color = self.options.pink_color
        black_color = self.options.black_color
        white_color = self.options.white_color

        box_width = self.options.box_width
        box_height = self.options.box_height
        text_size = self.options.text_size

    
        color_hex = "" #using a global variable to set what color the box is
        border_hex = "" #similiar to color hex, using global variable to define the outline color. 


        
        SVG_NS = "{http://www.w3.org/2000/svg}"

        # Create a group to hold the box and text
        layer = self.svg.get_current_layer()
        group = inkex.etree.SubElement(layer, SVG_NS + 'g', id=self.svg.get_unique_id('text_box_group_'))



        if box_color =="1":  #1 means green #when one option is selected, it will set the global variable color_hex to the predefined argument color, in this case green
            color_hex = green_color
        elif box_color == "2":  #2 means blue
            color_hex = blue_color
        elif box_color == "3":  #3 means pink
            color_hex = pink_color


        if border_color == "4":
            border_hex = black_color
        elif border_color == "5":
            border_hex = white_color



        # Create rectangle (box)
        rect_attribs = {
            'x': '0',
            'y': '0',
            'width': str(box_width),
            'height': str(box_height),
            'style': f'fill:{color_hex};stroke:{border_hex};stroke-width:1' #default as green, then try to swap the color depending on if the user selected something else

            
        }
        inkex.etree.SubElement(group, SVG_NS + 'rect', rect_attribs)



        # Create text element centered in the box
        text_attribs = {
            'x': str(box_width / 2),
            'y': str(box_height / 2),
            # center horizontally and vertically
            'style': f'font-size:{10};text-anchor:middle;dominant-baseline:middle;fill:#000000;font-family:Arial, Helvetica, sans-serif'
        }
        text_el = inkex.etree.SubElement(group, SVG_NS + 'text', text_attribs)
        text_el.text = text_content


if __name__ == '__main__':
    SetBoxPrototype1Extension().run()