#include <stdio.h>
#include <stdlib.h>
#include <python3.10/Python.h>

void print_python_list(PyObject *p) {
  if (!PyList_Check(p)) {
    fprintf(stderr, "Invalid Python list\n");
    return;
  }

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
  printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
}

void print_python_bytes(PyObject *p) {
  if (!PyBytes_Check(p)) {
    fprintf(stderr, "Invalid Python bytes\n");
    return;
  }

  printf("[*] Python bytes info\n");
  printf("[*] Size of the Python bytes = %ld\n", PyBytes_Size(p));

  printf("[*] Trying string: %s\n", PyBytes_AsString(p));
  printf("[*] First %d bytes:", 10);

  int i;
  for (i = 0; i < 10 && i < PyBytes_Size(p); i++) {
    printf(" %02x", (unsigned char)PyBytes_AsString(p)[i]);
  }
  printf("\n");
}
