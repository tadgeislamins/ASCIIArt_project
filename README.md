# ASCIIArt_project
### До 24.04:
   * Тася и Каролина
      * код, который принимает изображение любого разумного формата и размера (переводит в матрицу PyTorch, уменьшает относительно опр. ширины в ядра определённого размера)
      * бьёт его на кусочки и т.п., чтобы потом каждый кусочек (?) можно было преобразовать в один символ ASCII
      * переводит их в чб (разузнать, как устроен перевод в чб и насколько он убийственен для тех же линий-границ, которые потом хотелось бы мочь различать, когда будем со свёрточными это делать)

Дефолтная ширина (ASCII_width) - сколько символов в итоговом изображении хотим чтобы было.

• Сжимаем картинку до ширины tensor_width (30) × ASCII_width (надо выбрать, какую хотим)
• Делим сжатую картинку (тензор?) на тензоры 30×60
• ~Возвращает список тензоров

   * Арк
      * перевод символов ASCII в картинки и создание dataset-а (все символы ASCII чтобы лежали у нас уже в виде tensor-ов)
      * может быть, сразу и вычисление на основе этих картиночек средней плотности каждого символа
   * Артур
      * тг-бота научить получать изображение и выозвращать txt-файл, может быть, что-то ещё придумать и сделать что ему можно реализовать уже на данном этапе

### А [вот](http://wiki.cs.hse.ru/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B_%D0%B3%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F) вики иада
где есть про презы и тетрадки про сверточные сети и даже записи лекций жесть...
