#include <Python.h>

/**
 * print_python_list_info - Displays info on Python lists.
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int len = 0, alloc = 0, i = 0;
	PyObject *o;

	len = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", alloc);

	for (; i < len; i++)
	{
		printf("Element %d: ", i);
		o = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(o)->tp_name);
	}
}
