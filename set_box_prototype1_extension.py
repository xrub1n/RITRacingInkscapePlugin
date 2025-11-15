import inkex


class SetBoxPrototype1Extension(inkex.Effect):
    def add_arguments(self, pars):
        """Add extension parameters."""  
        pars.add_argument("--text_content", type=str, default="Sample Text", help="Text to display")
        pars.add_argument("--box_color_green", type=inkex.Boolean, default=True, help="Box fill color")
        pars.add_argument("--box_color_blue", type=inkex.Boolean, default=False, help="Box fill color")
        pars.add_argument("--box_color_pink", type=inkex.Boolean, default=False, help="Box fill color")
        pars.add_argument("--border_black_or_white", type=inkex.Boolean, default=False, help="Border black or white")
        pars.add_argument("--green_color", type=inkex.Color, default=inkex.Color("#b6d6a8"), help="Color green")  #setting each color up as a variable so it can be passed into other functions
        pars.add_argument("--blue_color", type=inkex.Color, default=inkex.Color("#2596be"), help="Color blue")
        pars.add_argument("--pink_color", type=inkex.Color, default=inkex.Color("#9d579"), help="Color pink")
        pars.add_argument("--white_color", type=inkex.Color, default=inkex.Color("#FFFFFF"), help="Color white")
        pars.add_argument("--black_color", type=inkex.Color, default=inkex.Color("#000000"), help="Color black")
        pars.add_argument("--box_width", type=int, default=60, help="Box width")
        pars.add_argument("--box_height", type=int, default=20, help="Box height")
        pars.add_argument("--text_size", type=int, default=7.5, help="Font size")

    def effect(self):
        """Main effect method called when extension is executed."""
        # Get parameters
        text_content = self.options.text_content
        box_color_green = self.options.box_color_green
        box_color_blue = self.options.box_color_blue   
        box_color_pink = self.options.box_color_pink
        border_black_or_white = self.options.border_black_or_white
        green_color = self.options.green_color
        blue_color = self.options.blue_color
        pink_color = self.options.pink_color
        black_color = self.options.black_color
        white_color = self.options.white_color
        box_width = self.options.box_width
        box_height = self.options.box_height
        text_size = self.options.text_size


        
        SVG_NS = "{http://www.w3.org/2000/svg}"

        # Create a group to hold the box and text
        layer = self.svg.get_current_layer()
        group = inkex.etree.SubElement(layer, SVG_NS + 'g', id=self.svg.get_unique_id('text_box_group_'))

        

        # Create rectangle (box)
        rect_attribs = {
            'x': '0',
            'y': '0',
            'width': str(box_width),
            'height': str(box_height),
            'style': f'fill:{green_color};stroke:{black_color};stroke-width:1' #default as green, then try to swap the color depending on if the user selected something else

            # if box_color_blue:
            #     elem.style.set_color(self.options.color_blue, 'fill')  #if blue was picked, swap the fill color to blue
            # else:
            #     pass  #otherwise just skip the function
            
            # if box_color_pink:
            #     elem.style.set_color(self.options.color_pink, 'fill') #same as blue
            # else:
            #     pass  #see blue else

            # if border_black_or_white:    #defaults to already being black
            #     pass                        
            # else:
            #     elem.style.set_color(self.options.color_white, 'stroke')   #if the user selects the box it turns the border white. Swap this from bool later
        }
        inkex.etree.SubElement(group, SVG_NS + 'rect', rect_attribs)



        # Create text element centered in the box
        text_attribs = {
            'x': str(box_width / 2),
            'y': str(box_height / 2),
            # center horizontally and vertically
            'style': f'font-size:{text_size}px;text-anchor:middle;dominant-baseline:middle;fill:#000000;font-family:Arial, Helvetica, sans-serif'
        }
        text_el = inkex.etree.SubElement(group, SVG_NS + 'text', text_attribs)
        text_el.text = text_content


if __name__ == '__main__':
    SetBoxPrototype1Extension().run()