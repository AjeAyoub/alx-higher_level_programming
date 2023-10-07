#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject representing the list.
 */
void print_python_list_info(PyObject *p);

int main(void) {
    Py_Initialize();
    
    // Create or obtain a PyObject representing a Python list
    PyObject *my_list = PyList_New(3);
    PyList_SetItem(my_list, 0, Py_BuildValue("i", 10));
    PyList_SetItem(my_list, 1, Py_BuildValue("s", "Hello"));
    PyList_SetItem(my_list, 2, Py_BuildValue("f", 3.14));

    // Call the function to print list info
    print_python_list_info(my_list);

    Py_Finalize();
    return 0;
}

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject representing the list.
 */
void print_python_list_info(PyObject *p) {
    int size, alloc, i;
    PyObject *obj;

    size = Py_SIZE(p);  // Get the size of the list
    alloc = ((PyListObject *)p)->allocated;  // Get the allocated memory

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size; i++) {
        printf("Element %d: ", i);

        obj = PyList_GetItem(p, i);  // Get the element at the current index
        printf("%s\n", Py_TYPE(obj)->tp_name);  // Print the type name of the element
    }
}
