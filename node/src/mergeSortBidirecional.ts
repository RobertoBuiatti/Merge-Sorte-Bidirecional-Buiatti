/**
 * Implementação do algoritmo Merge Sort Bidirecional em TypeScript
 * @author Roberto Buiatti
 */

/**
 * Função auxiliar para comparar elementos usando uma chave opcional
 */
function compareElements<T>(a: T, b: T, key?: (item: T) => any): boolean {
    if (key) {
        const keyA = key(a);
        const keyB = key(b);
        return keyA < keyB || (keyA === keyB); // Mantém a estabilidade
    }
    return a <= b;
}

/**
 * Ordena um array utilizando o algoritmo Merge Sort Bidirecional.
 * @param arr Array a ser ordenado
 * @param key Função opcional que especifica uma chave de ordenação personalizada
 */
export function mergeSortBidirecional<T>(arr: T[], key?: (item: T) => any): void {
    if (arr.length <= 1) {
        return;
    }

    const mid = Math.floor(arr.length / 2);
    const left = arr.slice(0, mid);
    const right = arr.slice(mid);

    // Ordena recursivamente as sublistas
    mergeSortBidirecional(left, key);
    mergeSortBidirecional(right, key);

    // Ponteiros para percorrer as sublistas
    let i = 0;
    let j = 0;
    let iRev = left.length - 1;
    let jRev = right.length - 1;

    const temp = new Array(arr.length);
    let front = 0;
    let back = arr.length - 1;

    while (front <= back) {
        // Processa elementos pelo início
        if (i <= iRev && (j > jRev || compareElements(left[i], right[j], key))) {
            temp[front] = left[i];
            i++;
            front++;
        } else if (j <= jRev) {
            temp[front] = right[j];
            j++;
            front++;
        }

        if (front > back) {
            break;
        }

        // Processa elementos pelo final
        if (iRev >= i && (jRev < j || !compareElements(left[iRev], right[jRev], key))) {
            temp[back] = left[iRev];
            iRev--;
            back--;
        } else if (jRev >= j) {
            temp[back] = right[jRev];
            jRev--;
            back--;
        }
    }

    // Copia os elementos ordenados de volta para o array original
    for (let k = 0; k < arr.length; k++) {
        arr[k] = temp[k];
    }
}
