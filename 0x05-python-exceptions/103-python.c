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

	int size = PyList_Size(p);

	printf("Size of the list: %d\n", size);

	for (int i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element at index %d: ", i);
		Pyobject_Print(item, stdout, 0);
		printf("\n");
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

	int size = PyBytes_Size(p);

	printf("Size of the bytes object: %d\n", size);

	printf("First 10 bytes: ");
	for (int i = 0; i < 10; i++)
	{
		printf("%02x ", PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
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

	printf("Value of the float: %f\n", value);
}
