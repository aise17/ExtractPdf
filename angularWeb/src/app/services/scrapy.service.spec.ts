import { TestBed } from '@angular/core/testing';

import { ScrapyService } from './scrapy.service';

describe('ScrapyService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: ScrapyService = TestBed.get(ScrapyService);
    expect(service).toBeTruthy();
  });
});
