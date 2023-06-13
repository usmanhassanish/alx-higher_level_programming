#include <Python.h>
/**
* print_python_list_info - print list info
* @p: object argument
*/
void print_python_list_info(PyObject *p)
{
        Py_ssize_t size, allocated;

        size = PyList_Size(p);
        allocated = ((PyListObject *)p)->allocated;

        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %zd\n", allocated);

        for (Py_ssize_t i = 0; i < size; i++)
        {
                PyObject *item = PyList_GetItem(p, i);
                const char *typeName = Py_TYPE(item)->tp_name;
                printf("Element %zd: %s\n", i, typeName);
        }
}
