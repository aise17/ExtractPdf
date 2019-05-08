import { TestBed } from '@angular/core/testing';

import { TrazasService } from './trazas.service';

describe('TrazasService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: TrazasService = TestBed.get(TrazasService);
    expect(service).toBeTruthy();
  });
});
