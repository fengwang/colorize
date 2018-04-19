CXX           = g++
CXXFLAGS      = -std=c++17 -O2 -Wall
LFLAGS        = -O2
OBJECTS_DIR   = .
BIN_DIR       = .
LINK 		  = $(CXX)

color: color_test.cc
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $(OBJECTS_DIR)/color.o ./color_test.cc
	$(LINK) $(LFLAGS) -o $(BIN_DIR)/color_test $(OBJECTS_DIR)/color.o

