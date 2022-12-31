#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - function that prints a python string
 * @p: pointer
 */
void print_python_string(PyObject *p)
{
	if (!PyUnicode_Check(p))
	{
		printf("Error: Object is not a string\n");
		return;
	}

	PyObject *temp = PyUnicode_AsEncodedString(p, "utf-8", "strict");

	if (temp == NULL)
	{
		printf("Error: Failed to encode string\n");
		return;
	}

	char *str = PyBytes_AsString(temp);

	printf("string object info\n");
	printf("  type: %s\n", PyUnicode_IS_ASCII(p) ? "compact ascii" : "unicode");
	printf("  length: %ld\n", PyUnicode_GetLength(p));
	printf("  value: %s\n", str);

	Py_DECREF(temp);
}
