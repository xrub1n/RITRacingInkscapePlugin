import inkex


class SetBoxPrototype1Extension(inkex.Effect):
    def add_arguments(self, pars):
        """Add extension parameters."""
        pars.add_argument("--text_content", type=str, default="Sample Text", help="Text to display")
        pars.add_argument("--box_color_green", type=inkex.Boolean, default=True, help="Box fill color")
        pars.add_argument("--box_color_blue", type=inkex.Boolean, default=False, help="Box fill color")
        pars.add_argument("--box_color_pink", type=inkex.Boolean, default=False, help="Box fill color")
        pars.add_argument("--border_black_or_white", type=inkex.Boolean default=inkex.style(""))
        pars.add_argument("--box_width", type=int, default=60, help="Box width")
        pars.add_argument("--box_height", type=int, default=20, help="Box height")
        pars.add_argument("--text_size", type=int, default=7.5, help="Font size")

    def effect(self):
        """Main effect method called when extension is executed."""
        # Get parameters
        text_content = self.options.text_content
        box_color_green = self.options.box_color_green
        box_color_blue = self.options.box_color_green   #code so only ONE of the color options may be true at any given time
        box_color_pink = self.options.box_color_green
        border_black_or_white = self.options.border_black_or_white
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
            'style': f'fill:{box_color};stroke:#000000;stroke-width:5'
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