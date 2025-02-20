import { mergeSortBidirecional } from '../src/mergeSortBidirecional';

describe('Testes Completos do MergeSortBidirecional', () => {
    const logTest = (name: string, expected: any, received: any) => {
        console.log(`\nTeste: ${name}`);
        console.log(`Esperado: ${JSON.stringify(expected)}`);
        console.log(`Obtido  : ${JSON.stringify(received)}`);
        console.log(`Resultado: ${JSON.stringify(expected) === JSON.stringify(received) ? '✓' : '✗'}`);
    };

    test('Números inteiros', () => {
        const arr = [64, 34, 25, 12, 22, 11, 90];
        const expected = [...arr].sort((a, b) => a - b);
        mergeSortBidirecional(arr);
        logTest('Números inteiros', expected, arr);
        expect(arr).toEqual(expected);
    });

    test('Números repetidos', () => {
        const arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
        const expected = [...arr].sort((a, b) => a - b);
        mergeSortBidirecional(arr);
        logTest('Números repetidos', expected, arr);
        expect(arr).toEqual(expected);
    });

    test('Strings', () => {
        const arr = ['banana', 'maçã', 'uva', 'pera'];
        const expected = [...arr].sort();
        mergeSortBidirecional(arr);
        logTest('Strings', expected, arr);
        expect(arr).toEqual(expected);
    });

    test('Strings por tamanho', () => {
        const arr = ['banana', 'maçã', 'uva', 'pera'];
        const expected = [...arr].sort((a, b) => a.length - b.length);
        mergeSortBidirecional(arr, str => str.length);
        logTest('Strings por tamanho', expected, arr);
        expect(arr).toEqual(expected);
    });

    test('Lista vazia', () => {
        const arr: number[] = [];
        mergeSortBidirecional(arr);
        logTest('Lista vazia', [], arr);
        expect(arr).toEqual([]);
    });

    test('Um elemento', () => {
        const arr = [42];
        mergeSortBidirecional(arr);
        logTest('Um elemento', [42], arr);
        expect(arr).toEqual([42]);
    });

    test('Objetos complexos', () => {
        interface Pessoa {
            nome: string;
            idade: number;
        }

        const arr: Pessoa[] = [
            { nome: 'João', idade: 25 },
            { nome: 'Maria', idade: 30 },
            { nome: 'Ana', idade: 20 },
            { nome: 'Pedro', idade: 35 },
            { nome: 'Clara', idade: 28 }
        ];

        const expected = [...arr].sort((a, b) => a.idade - b.idade);
        mergeSortBidirecional(arr, p => p.idade);
        logTest('Objetos', expected, arr);
        expect(arr).toEqual(expected);
    });

    test('Estabilidade na ordenação', () => {
        interface Item {
            valor: number;
            indice: number;
        }

        const arr: Item[] = [
            { valor: 3, indice: 1 },
            { valor: 3, indice: 2 },
            { valor: 3, indice: 3 },
            { valor: 1, indice: 4 },
            { valor: 2, indice: 5 }
        ];

        const expected = [
            { valor: 1, indice: 4 },
            { valor: 2, indice: 5 },
            { valor: 3, indice: 1 },
            { valor: 3, indice: 2 },
            { valor: 3, indice: 3 }
        ];

        mergeSortBidirecional(arr, item => item.valor);
        logTest('Estabilidade', expected, arr);
        expect(arr).toEqual(expected);
    });
});
