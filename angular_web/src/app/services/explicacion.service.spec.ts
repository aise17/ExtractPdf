import { TestBed } from '@angular/core/testing';

import { ExplicacionService } from './explicacion.service';

describe('ExplicacionService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ExplicacionService = TestBed.get(ExplicacionService);
    expect(service).toBeTruthy();
  });
});
