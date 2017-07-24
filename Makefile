CXX           = clang++
CXXFLAGS        = -std=c++1z -stdlib=libc++ -O3 -ferror-limit=2 -Weverything -Wno-c++98-compat -Wno-c++98-compat-pedantic -Wno-sign-conversion -Wno-exit-time-destructors -Wno-float-equal -Wno-global-constructors -Wno-missing-declarations -Wno-unused-parameter -Wno-padded -Wno-shadow -Wno-weak-vtables -Wno-missing-prototypes -Wno-unused-variable -ferror-limit=1 -Wno-deprecated -Wno-conversion -Wno-double-promotion
LFLAGS        = -lc++ -lc++abi -O3
OBJECTS_DIR   = .
BIN_DIR       = .
LINK 		  = $(CXX)

color: color_test.cc
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $(OBJECTS_DIR)/color.o ./color_test.cc
	$(LINK) $(LFLAGS) -o $(BIN_DIR)/color_test $(OBJECTS_DIR)/color.o

