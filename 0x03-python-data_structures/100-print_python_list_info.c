#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Function to print some basic
 * info about a Python list
 * @p: elemets of a python list
 */
void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Error: Input is not a Python list\n");
		return;
	}

	int size = PyList_Size(p);

	printf("[*] Size of the Python List = %d\n", size);

	printf("[*] All elements of the Python List:\n");

	for (int i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %d: %s\n", i, PyUnicode_AsUTF8(PyObject_Repr(item)));
	}
}
