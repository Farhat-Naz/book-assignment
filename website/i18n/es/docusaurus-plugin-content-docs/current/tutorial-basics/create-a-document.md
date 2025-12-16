---
sidebar_position: 2
---

# Crear un documento

Los documentos son **grupos de páginas** conectadas a través de:

- una **barra lateral**
- ** navegación anterior/siguiente **
- **control DEversiones**

## Crea tu primer documento

Crear un archivo Markdown en`docs/hello.md`:```md title="docs/hello.md"
# Hello

This is my **first Docusaurus document**!
```Ya está disponible un nuevo documento en [http://localhost:3000/docs/hello](http://localhost:3000/docs/hello).

## Configurar la barra lateral

Docusaurus crea automáticamente ** una barra lateral** desde el`docs`carpeta.

Añade metadatos para personalizar la etiqueta y la posición de la barra lateral:```md title="docs/hello.md" {1-4}
---
sidebar_label: 'Hi!'
sidebar_position: 3
---

# Hello

This is my **first Docusaurus document**!
```También es posible crear su barra lateral explícitamente en`sidebars.js`:```js title="sidebars.js"
export default {
  tutorialSidebar: [
    'intro',
    // highlight-next-line
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
};
```
