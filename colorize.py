#!/bin/env python3.8

color_foreground = {
    'Default': '39',
    'Black': '30',
    'Red': '31',
    'Green': '32',
    'Yellow': '33',
    'Blue': '34',
    'Magenta': '35',
    'Cyan': '36',
    'Light Gray': '37',
    'Dark Gray': '90',
    'Light Red': '91',
    'Light Green': '92',
    'Light Yellow': '93',
    'Light Blue': '94',
    'Light Magenta': '95',
    'Light Cyan': '96',
    'White': '97'
}

color_background = {
    'Default': '49',
    'Black': '40',
    'Red': '41',
    'Green': '42',
    'Yellow': '43',
    'Blue': '44',
    'Megenta': '45',
    'Cyan': '46',
    'Light Gray': '47',
    'Dark Gray': '100',
    'Light Red': '101',
    'Light Green': '102',
    'Light Yellow': '103',
    'Light Blue': '104',
    'Light Magenta': '105',
    'Light Cyan': '106',
    'White': '107'
}

formatting_set = {
    'Default': '0',
    'Bold': '1',
    'Dim': '2',
    'Underlined': '4',
    'Blink': '5',
    'Reverse': '7',
    'Hidden': '8'
}

formatting_reset = {
    'All': '0',
    'Bold': '21',
    'Dim': '22',
    'Underlined': '24',
    'Blink': '25',
    'Reverse': '27',
    'Hidden': '28'
}

def colorize(source,
             foreground_color='Default',
             background_color='Default',
             set_formatting='Default',
             reset_formatting='Default'):
    control = '\033'
    global color_foreground

    if not foreground_color in color_foreground:
        foreground_color = 'Default'

    if not background_color in color_background:
        background_color = 'Default'

    if not set_formatting in formatting_set:
        set_formatting = 'Default'

    if not reset_formatting in formatting_reset:
        reset_formatting = 'All'

    return f'{control}[{formatting_set[set_formatting]};{color_background[background_color]};{color_foreground[foreground_color]}m{source}{control}[{formatting_reset[reset_formatting]}m'


if __name__ == '__main__':

    def demo(source, foreground_color, background_color, set_formatting,
             reset_formatting):
        print( f'\'colorize({source=}, {foreground_color=}, {background_color=}, {set_formatting=}, {reset_formatting=})\' generating')
        print( colorize(source, foreground_color, background_color, set_formatting, reset_formatting))

    source = 'I am a Banana!'
    for _, foreground_color in enumerate(color_foreground):
        for _, background_color in enumerate(color_background):
            for _, set_formatting in enumerate(formatting_set):
                reset_formatting = 'Default'
                demo(source, foreground_color, background_color,
                     set_formatting, reset_formatting)
                #for _, reset_formatting in enumerate(formatting_reset):
                #    demo( source, foreground_color, background_color, set_formatting, reset_formatting )
