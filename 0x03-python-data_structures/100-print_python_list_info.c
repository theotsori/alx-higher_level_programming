#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Function to print some basic
 * info about a Python list
 * @p: elemets of a python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
}
