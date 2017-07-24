#include "./color.hpp"

#include <iostream>

int main()
{
    auto const& generate = []( std::string const & source, std::string const & fore, std::string const & back, std::string const & set, std::string const & reset )
    {
        if ( fore == back ) return;
        std::cout << "color::rize(\"" << source  << "\", \"" << fore  << "\", \"" << back  << "\", \"" << set << "\") results in\n" << color::rize( source, fore, back, set, reset ) << "\n\n";
    };

    std::string const message{ "I am a banana!" };

    for ( auto [set, code_set] : color::formatting_set )
        for ( auto [fore, code_fore] : color::color_foreground )
            for ( auto [back, code_back] : color::color_background )
            {
                std::string reset = "All";
                generate( message, fore, back, set, reset );
            }

    return 0;
}

