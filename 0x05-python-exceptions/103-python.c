#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - function to print basic info
 * @p: pointer
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("Error: p is not a valid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);

	printf("Number of elements in the list: %zd\n", size);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element at index %zd: %s\n", i, PyUnicode_AsUTF8(item));
	}
}
/**
 * print_python_bytes - function to print basic py bytes object
 * @p: pointer
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("Error: p is not a valid PyBytesObject\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("Number of bytes in the object: %zd\n", size);

	if (size >= 10)
	{
		printf("First 10 bytes: ");
		for (int i = 0; i < 10; i++)
		{
			printf("%02x ", PyBytes_AS_STRING(p)[i]);
		}
		printf("\n");
	}
}
/**
 * print_python_float - function to print py float objects
 * @p: pointer
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("Error: p is not a valid PyFloatObject\n");
		return;
	}

	double value = PyFloat_AS_DOUBLE(p);

	printf("Value of the float object: %f\n", value);
}
