// glad / glfw library include statements
#include <glad/glad.h>
#include <GLFW/glfw3.h>

// other libs

#include <iostream>
#include <future>



// functions and stuff


int main() {












    // start rendering (should be at end)

    // init glfw
    if (!glfwInit()) {
        std::cout << "Failed to init GLFW\n";
        return -1;
    }

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);

    // create window
    GLFWwindow* window = glfwCreateWindow(800, 600, "OpenGL Window", NULL, NULL);
    if (!window) {
        std::cout << "Failed to create window\n";
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window);

    // load openGL glad
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cout << "Failed to initialize GLAD\n";
        return -1;
    }

    // image test 

    stbi_set_flip_vertically_on_load(true);

    int w, h, ch;
    unsigned char* test = stbi_load("test.png", &w, &h, &ch, 4);

    if (!test) {
        std::cout << "FAILED TO LOAD IMAGE\n";
    }

    // set viewport
    glViewport(0, 0, 1200, 1200);

    // render loop
    while (!glfwWindowShouldClose(window)) {
        // backgound bluu
        glClearColor(0.1f, 0.1f, 0.2f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwTerminate();
    return 0;
}