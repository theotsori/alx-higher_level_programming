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
		fprintf(stderr, "Error: Invalid PyListObject\n");
		return;
	}

	int size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	int i;

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
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
		fprintf(stderr, "Error: Invalid PyBytesObject\n");
		return;
	}

	int size = PyBytes_Size(p);

	printf("[*] Python bytes info\n");
	printf("[*] Size of the Python bytes = %d\n", size);
	printf("[*] First %d bytes: ", size > 10 ? 10 : size);

	int i;

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	putchar('\n');
}
/**
 * print_python_float - function to print py float objects
 * @p: pointer
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Error: Invalid PyFloatObject\n");
		return;
	}

	double value = PyFloat_AS_DOUBLE(p);

	printf("[*] Python float info\n");
	printf("[*] Value of the Python float: %f\n", value);
}

