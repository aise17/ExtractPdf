import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FormScrapyComponent } from './form-scrapy.component';

describe('FormScrapyComponent', () => {
  let component: FormScrapyComponent;
  let fixture: ComponentFixture<FormScrapyComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FormScrapyComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FormScrapyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
