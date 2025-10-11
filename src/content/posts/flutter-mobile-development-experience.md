---
title: "Building Mobile Apps with Flutter: Lessons from TehIbu Project"
description: "Key insights and lessons learned while developing the TehIbu mobile application using Flutter during my internship at Makerindo."
date: 2023-02-20
author: "Firdaus Nuur Rhamadhan"
image: ""
tags:
  - Flutter
  - Mobile Development
  - Dart
  - UI/UX
  - REST API
category: "Mobile Development"
draft: false
---

# Building Mobile Apps with Flutter: Lessons from TehIbu Project

During my internship at Makerindo, I had the opportunity to work on the TehIbu mobile application using Flutter. This experience taught me invaluable lessons about mobile development, cross-platform frameworks, and building production-ready applications.

## Why Flutter?

Flutter's appeal lies in its ability to create beautiful, natively compiled applications from a single codebase. Key advantages I discovered:

- **Hot Reload**: Instant feedback during development accelerates iteration
- **Rich Widget Library**: Pre-built Material and Cupertino widgets for consistent UI
- **Performance**: Compiled to native ARM code for smooth 60fps animations
- **Single Codebase**: Write once, deploy to iOS and Android

## Project Overview: TehIbu App

The TehIbu application required a modern, responsive interface with seamless backend integration. My responsibilities included:

1. **UI Implementation**: Translating design mockups into Flutter widgets
2. **State Management**: Managing app state efficiently
3. **API Integration**: Connecting frontend with REST API backend
4. **Testing**: Ensuring reliability across different devices

## Key Technical Decisions

### State Management
I chose Provider for state management due to its simplicity and official recommendation. It provided:
- Clear separation of business logic and UI
- Easy testing and maintainability
- Minimal boilerplate code

### API Integration
Using the `http` package with proper error handling:
```dart
Future<List<Product>> fetchProducts() async {
  try {
    final response = await http.get(Uri.parse('$baseUrl/products'));
    if (response.statusCode == 200) {
      return parseProducts(response.body);
    }
  } catch (e) {
    // Handle errors gracefully
  }
}
```

## Challenges Faced

### 1. Responsive Design
Creating layouts that work across various screen sizes required:
- Using `MediaQuery` for dynamic sizing
- Implementing flexible layouts with `Flex` widgets
- Testing on multiple device sizes

### 2. Backend Integration
Coordinating with the backend team taught me:
- Importance of clear API documentation
- Handling loading states and errors gracefully
- Implementing proper authentication flows

### 3. Performance Optimization
Ensuring smooth performance involved:
- Lazy loading for large lists
- Image caching and optimization
- Minimizing unnecessary rebuilds

## Best Practices Learned

1. **Widget Composition**: Break down complex UIs into reusable widgets
2. **Separation of Concerns**: Keep business logic separate from UI code
3. **Error Handling**: Always handle edge cases and network failures
4. **User Feedback**: Provide clear loading indicators and error messages

## Reflection

Working on TehIbu was my first serious mobile development project, and it solidified my interest in cross-platform development. Flutter's developer experience is exceptional, and the community support is outstanding.

## What's Next?

I'm eager to explore:
- Advanced state management solutions (Riverpod, BLoC)
- Flutter for web and desktop
- Custom animations and transitions
- Integration with device features (camera, GPS, sensors)

Mobile development with Flutter has opened up new possibilities in my career, and I'm excited to build more applications that deliver great user experiences!
