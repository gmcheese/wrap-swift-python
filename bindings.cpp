#include <pybind11/pybind11.h>

namespace py = pybind11;

// C++ wrapper for the Swift function
extern "C" {
    int add(int a, int b); // Declaration of the Swift function
}

PYBIND11_MODULE(mymodule, m) {
    m.def("add", &add, "A function that adds two numbers");
}
