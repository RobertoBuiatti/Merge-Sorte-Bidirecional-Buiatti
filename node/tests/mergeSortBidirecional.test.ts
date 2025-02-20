import { mergeSortBidirecional } from '../src/mergeSortBidirecional';

describe('MergeSortBidirecional', () => {
    it('deve ordenar um array de números', () => {
        const arr = [64, 34, 25, 12, 22, 11, 90];
        mergeSortBidirecional(arr);
        expect(arr).toEqual([11, 12, 22, 25, 34, 64, 90]);
    });

    it('deve manter um array vazio inalterado', () => {
        const arr: number[] = [];
        mergeSortBidirecional(arr);
        expect(arr).toEqual([]);
    });

    it('deve manter um array de um elemento inalterado', () => {
        const arr = [1];
        mergeSortBidirecional(arr);
        expect(arr).toEqual([1]);
    });

    it('deve ordenar um array com elementos repetidos', () => {
        const arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
        mergeSortBidirecional(arr);
        expect(arr).toEqual([1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]);
    });

    it('deve ordenar um array de strings', () => {
        const arr = ['banana', 'maçã', 'uva', 'pera'];
        mergeSortBidirecional(arr);
        expect(arr).toEqual(['banana', 'maçã', 'pera', 'uva']);
    });

    it('deve ordenar usando uma função de chave personalizada', () => {
        const arr = ['banana', 'maçã', 'uva', 'pera'];
        mergeSortBidirecional(arr, str => str.length);
        expect(arr).toEqual(['uva', 'pera', 'maçã', 'banana']);
    });

    it('deve ordenar objetos usando uma chave personalizada', () => {
        interface Pessoa {
            nome: string;
            idade: number;
        }

        const arr: Pessoa[] = [
            { nome: 'João', idade: 25 },
            { nome: 'Maria', idade: 30 },
            { nome: 'Ana', idade: 20 }
        ];

        mergeSortBidirecional(arr, pessoa => pessoa.idade);

        expect(arr).toEqual([
            { nome: 'Ana', idade: 20 },
            { nome: 'João', idade: 25 },
            { nome: 'Maria', idade: 30 }
        ]);
    });
});
