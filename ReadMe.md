## String-Colorization Library for Terminal Output

#### Basic colorize function call

```
std::string const& colorized_string =
color::rize( ORIGINAL_STRING,
             A_FOREGROUND_COLOR_STRING, 
             A_BACKGROUND_COLOR_STRING );
```

#### Example Usage:

```
//example.cpp
std::string message{"I am a Banana."};
// Output message with 
//              foreground color -- Yellow
//              background color -- Green
std::cout   << color::rize( message, "Yellow", "Green" )
            << std::endl;
```

#### Compilation command:

```
g++ -o example example.cpp -std=c++17
```

#### Availiable colors:

+ `Default`
+ `Black`
+ `Red`
+ `Green`
+ `Yellow`
+ `Blue`
+ `Magenta`
+ `Cyan`
+ `Light Grey`
+ `Dark Grey`
+ `Light Red`
+ `Light Green`
+ `Light Yellow`
+ `Light Blue`
+ `Light Magenta`
+ `Light Cyan`
+ `White`

#### More Example

with function

```
std::string const& colorized_string =
color::rize( ORIGINAL_STRING,
             A_FOREGROUND_COLOR_STRING, 
             A_BACKGROUND_COLOR_STRING,
             A_ATTRIBUTE_STRING );
```

where the third parameter `attribute` can be

+ `Default`
+ `Bold`
+ `Dim`
+ `Underlined`
+ `Blink`
+ `Reverse`
+ `Hidden`

and an some of the examples





