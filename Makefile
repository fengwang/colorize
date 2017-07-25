CXX           = clang++
CXXFLAGS        = -std=c++1z -stdlib=libc++ -O3 -ferror-limit=2 -Weverything
LFLAGS        = -lc++ -lc++abi -O3
OBJECTS_DIR   = .
BIN_DIR       = .
LINK 		  = $(CXX)

color: color_test.cc
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $(OBJECTS_DIR)/color.o ./color_test.cc
	$(LINK) $(LFLAGS) -o $(BIN_DIR)/color_test $(OBJECTS_DIR)/color.o

