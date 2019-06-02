import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NormasScrapyComponent } from './normas-scrapy.component';

describe('NormasScrapyComponent', () => {
  let component: NormasScrapyComponent;
  let fixture: ComponentFixture<NormasScrapyComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NormasScrapyComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NormasScrapyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
