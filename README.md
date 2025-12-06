![PS4 Templates](./Assets/header.png)

A Visual Studio template bundle for the official PS4 SDK. Quickly scaffold SPRX and ELF eboot projects with automatic fself scripts and StubMaker integration.

## Features

- **SPRX Project Template**: PS4 module project
- **ELF Eboot Template**: Standalone executable project
- **Automatic fself Scripts**: `make_fself.py` included in Scripts folder
- **StubMaker Ready**: Pre-configured External folder for StubMaker
- **Precompiled Headers**: Standardized library management across configurations

## Installation

1. Download the latest `.vsix` from Releases
2. Double-click to install (requires Visual Studio 2022/2026)
3. Wait for "Updating configuration" to complete (this can take 1-2 minutes)

## Creating a Project

1. Open Visual Studio
2. **File → New → Project**
3. Search for "PS4"
4. Select your template (SPRX or ELF)
5. After creation, set up your dependencies:

```powershell
# Option A: Initialize git and add StubMaker as submodule
cd YourProject
git init
git submodule add https://github.com/OSM-Made/StubMaker.git External/StubMaker

# Option B: Just clone StubMaker directly
git clone https://github.com/OSM-Made/StubMaker.git External/StubMaker
```

## Project Structure

```
YourProject/
├── YourProject.sln
├── YourProject/
│   ├── YourProject.vcxproj
│   ├── stdafx.h          # Precompiled header - includes
│   ├── stdafx.cpp        # Precompiled header - library links
│   └── main.cpp/prx.cpp
├── Scripts/
│   └── make_fself.py     # Fake self signing script
└── External/
    └── StubMaker/        # Clone or submodule here
```

## Precompiled Header Setup

The templates use a standardized precompiled header approach for easy library management:

### stdafx.h
Add your system includes and headers here:

```cpp
#pragma once
#include <kernel.h>
#include <string>
#include <queue>
#include <vector>
#include <mutex>
#include <variant>
// Add more system libs here...

// StubMaker
#include <KernelExt.h>

// Your project libs
// #include <...>
```

### stdafx.cpp
Link your libraries here:

```cpp
#include "stdafx.h"

// Standard Libraries
#pragma comment(lib, "libSceLibcInternal_gen_stub_weak.a")
#pragma comment(lib, "libkernel_stub_weak.a")
#pragma comment(lib, "libkernel_gen_stub_weak.a")

// Additional Libraries
// #pragma comment(lib, "...")
```

This approach keeps library management consistent across Debug/Release configurations and makes it easy to see all dependencies in one place.

## Uninstalling

1. **Extensions → Manage Extensions**
2. Find "PS4 Templates" and click Uninstall
3. Restart Visual Studio
4. If VS has issues starting, run:
   ```cmd
   devenv /updateconfiguration
   ```

## Requirements

- Visual Studio 2022 or 2026
- Official PS4 SDK
- [StubMaker](https://github.com/OSM-Made/StubMaker)
