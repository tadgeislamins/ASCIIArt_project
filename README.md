# ASCIIArt_project
До 24.04:
   * Тася и Каролина
      * код, который принимает изображение любого разумного формата и размера (переводит в матрицу PyTorch, уменьшает относительно опр. ширины в ядра определённого размера)
      * переводит его в чб (разузнать, как устроен перевод в чб и насколько он убийственен для тех же линий-границ, которые потом хотелось бы мочь различать, когда будем со свёрточными это делать)
      * бьёт его на кусочки и т.п., чтобы потом каждый кусочек (?) можно было преобразовать в один символ ASCII
   * Арк
      * перевод символов ASCII в картинки и создание dataset-а (все символы ASCII чтобы лежали у нас уже в виде tensor-ов)
      * может быть, сразу и вычисление на основе этих картиночек средней плотности каждого символа
   * Артур
      * тг-бота научить получать изображение и выозвращать txt-файл, может быть, что-то ещё придумать и сделать что ему можно реализовать уже на данном этапе
