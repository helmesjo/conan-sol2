[![Download](https://api.bintray.com/packages/helmesjo/public-conan/sol2%3Ahelmesjo/images/download.svg) ](https://bintray.com/helmesjo/public-conan/sol2%3Ahelmesjo/_latestVersion)
[![Build Status Travis](https://travis-ci.org/helmesjo/conan-sol2.svg?branch=stable%2F3.0.3)](https://travis-ci.com/helmesjo/conan-sol2)
[![Build Status AppVeyor](https://ci.appveyor.com/api/projects/status/github/helmesjo/conan-sol2?branch=stable%2F3.0.3&svg=true)](https://ci.appveyor.com/project/helmesjo/conan-sol2)

## Conan package recipe for [*sol2*](https://github.com/ThePhD/sol2)

sol is a C++ library binding to Lua.

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/helmesjo/public-conan/sol2%3Ahelmesjo).


## Issues

If you wish to report an issue or make a request for a package, please do so here:

[Issues Tracker](https://github.com/bincrafters/community/issues)


## For Users

### Basic setup

    $ conan install sol2/3.0.3@helmesjo/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    sol2/3.0.3@helmesjo/stable

    [generators]
    txt

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . helmesjo/stable




## Add Remote

    $ conan remote add helmesjo "https://api.bintray.com/conan/helmesjo/public-conan"


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package sol2.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](https://github.com/helmesjo/conan-sol2/blob/stable/3.0.3/LICENSE.md)
