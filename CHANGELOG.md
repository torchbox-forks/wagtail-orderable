# Change Log

## Unreleased

- Drop support for Wagtail < 6.3
- Drop support for Django < 4.2 and add support for Django 5.1 and 5.2
- Drop support for Python < 3.9 and add support for Python 3.13 and 3.14
- Wagtail 7.2 support
- Wagtail 7.1 support
- Wagtail 7.0 support
- Wagtail 6.4 support
- Wagtail 6.3 support
- Wagtail 6.2 support

- Wagtail 6.1 support
- Drop support for Django < 4.2

1.3.0+tbx
---

- Wagtail 6.0 support

1.2.0
---

- Updated documentation for wagtail 4.0 support
- Updated workflow action versions
- Allow wagtail v4.1+ (drops ability to use on a wagtail site version earlier than v4.1)
- Allow Wagtail v5 and Django v4.2

1.1.0
---

- Extending `Orderable` is no more mandatory if you want to use your own order field (#27)
- Add `Orderable.get_sort_order_max()` to get the max "order" when instance is being created (#27)
- Fix keeping current filters when sorting was reset (#27)
- Fix class names (`get_extra_class_names_for_field_col` parameters were inverted) (#27)
- Fix CSS which had SCSS syntax (#27)

1.0.4
---

- Provide Github Actions script to build and publish package in PyPI
- Add support for Wagtail 3.0 and drop support for all Wagtail versions
   before 2.15 (#32)
- Use `pk` instead of `id` for duplicate positions (#31)

1.0.3
---

- Fix `TypeError` when creating the first Orderable object (#21)

1.0.2
---

- Fix `sort_order` duplication for items
- Fix wrong `return` syntax

1.0.1
---

- `get_list_display` handles any iterable
- Support for filters in ModelAdmin
- Style updated
