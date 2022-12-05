#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints info about a Python list object
 * @p: pointer to PyObject representing a Python list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
