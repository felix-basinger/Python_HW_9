import text
import view
import model


# 1. Добавлена функция изменения (изменяет контакт полностью, частями не удалось реализовать)
# 2. Добавлена функция удаления (удаляет первый найденный контакт в справочнике)


def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
                view.print_message(text.add_successful(new.get("name")))
            case 5:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.search_word()
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))

                if len(result) > 0:
                    model.contact_changes(result, view.add_changes())
                else:
                    view.print_message(text.changes_error)
            case 7:
                word = view.search_word()
                result = model.search(word)

                model.delete(result)
                view.show_del(result, text.del_mess(word))
            case 8:
                view.print_message(text.bye_message)
                break
