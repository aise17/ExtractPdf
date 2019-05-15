import { TestBed } from '@angular/core/testing';

import { BonoUsuarioService } from './bono-usuario.service';

describe('BonoUsuarioService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: BonoUsuarioService = TestBed.get(BonoUsuarioService);
    expect(service).toBeTruthy();
  });
});
