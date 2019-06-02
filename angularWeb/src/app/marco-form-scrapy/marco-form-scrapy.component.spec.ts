import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MarcoFormScrapyComponent } from './marco-form-scrapy.component';

describe('MarcoFormScrapyComponent', () => {
  let component: MarcoFormScrapyComponent;
  let fixture: ComponentFixture<MarcoFormScrapyComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MarcoFormScrapyComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MarcoFormScrapyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
