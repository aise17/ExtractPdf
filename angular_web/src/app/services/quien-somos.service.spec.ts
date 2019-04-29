import { TestBed } from '@angular/core/testing';

import { QuienSomosService } from './quien-somos.service';

describe('QuienSomosService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: QuienSomosService = TestBed.get(QuienSomosService);
    expect(service).toBeTruthy();
  });
});
